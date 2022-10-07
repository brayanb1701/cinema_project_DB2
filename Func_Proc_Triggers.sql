-- Actualiza el saldo en cliente cuando se recargue un valor a la tarjeta
DELIMITER :)
CREATE TRIGGER actualizar_saldo AFTER INSERT
ON recarga FOR EACH ROW 
BEGIN
update cliente set saldo=saldo+new.valor where identificacion=new.fk_identificacion;
END :)
DELIMITER ;

-- Funcion que calcula el valor del tiquete dependiendo si la sala es de soporte 3D o DI
DELIMITER :)
CREATE FUNCTION mirar_soporte_sala(vis int) RETURNS float READS SQL DATA
begin
declare soporte char(2);
set soporte = (select distinct s.soporte from  visualiza v 
inner join proyecta p on v.fk_codigo_proyecta=p.codigo_f
inner join sala s on s.codigo_sala=p.fk_codigo_sala WHERE v.codigo_v=vis);
CASE
    WHEN soporte='DI' THEN RETURN 8000;
    WHEN soporte='3D' THEN RETURN 12000;
END CASE;
END :)
DELIMITER ;

-- Costo de la entrada para ver contenido multimedia
DELIMITER :)
CREATE TRIGGER entrada BEFORE INSERT
ON visualiza FOR EACH ROW 
BEGIN
declare tipo float;
set tipo=(select  mirar_soporte_sala(new.codigo_v));
set new.total=tipo*new.cantidad;
update cliente set saldo=saldo-new.total where identificacion=new.fk_identificacion;
END :)
DELIMITER ;

-- Funcion que calcula el valor total de las comidas compradas
DELIMITER :)
CREATE FUNCTION total_comida(codigo int, cantidad int) RETURNS float READS SQL DATA
begin
declare valor float ;
set valor = (select distinct o.valor_comida from compra c
inner join comidas o on o.codigo_comida=codigo)*cantidad;
return valor;
END :)
DELIMITER ;

-- Cobro total comida
DELIMITER :)
CREATE TRIGGER descontar_saldo_comida AFTER INSERT
ON compra FOR EACH ROW 
BEGIN
update cliente set saldo=saldo-(select total_comida(new.fk_codigo_comida,new.cant_com)) where identificacion=new.fk_identificacion;
END :)
DELIMITER ;