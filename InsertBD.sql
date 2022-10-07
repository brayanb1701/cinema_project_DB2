USE proyecto_cine;

INSERT INTO sede_cine(nombre,zona,hora_apertura,hora_cierre)
VALUES
('Cine Woolands-Sense', 'Zona Sur','09:00:00','23:00:00'),
('Cine Woolands-Golden', 'Zona Norte','08:00:00','24:00:00' ),
('Cine Woolands-Multiplex', 'Zona Oriente','10:00:00','01:00:00'),
('Cine Woolands-Stellar', 'Zona Occidente','09:00:00','24:00:00'),
('Cine', '0','00:00:00','24:00:00');

INSERT INTO comidas(codigo_comida,valor_comida,nombre,descrip_comida)
VALUES
(101,23600,'COMBO 1','2 gaseosas grandes 1280 ml (cada una) + 1 crispeta grande 150 g'),
(102,20500,'COMBO 2','2 gaseosas medianas 960 ml (cada una) + 1 crispeta mediana 120 g'),
(103,33200,'COMBO 3','2 gaseosas medianas 960 ml (cada una) + 1 crispeta mediana 120 g+ 2 perros calientes o sándwich'),
(104,20700,'COMBO 4','1 gaseosa mediana 960 ml + 1 crispeta pequeña 100 g+ 1 perro caliente o sándwich'),
(201,13900,'CRISPETA GRANDE','170 Oz (sal)'),
(202,11300,'CRISPETA MEDIANA','130 Oz (sal)'),
(203,9400,'CRISPETA PEQUEÑA','85 Oz (sal)'),
(301,8200,'PERRO CALIENTE','sencillo'),
(302,8200,'SANDWICH','sencillo'),
(303,8200,'NACHOS CON QUESO','sencillos'),
(304,3900,'ADICIÓN QUESO NACHOS','sencilla'),
(401,7000,'GASEOSA GRANDE','44 Oz'),
(402,6200,'GASEOSA MEDIANA','32 Oz'),
(403,5400,'GASEOSA PEQUEÑA', '22 Oz'),
(404,3900,'AGUA CRISTAL','600 ml'),
(501,4200,'TURRÓN JOHNNY´S','48 g'),
(502,5400,'Milo Nuggets','40 g'),
(503,3200,'Cocosette Maxi Wafer','50 g'),
(504,6900,'M&Ms','48 g');

INSERT INTO sala(codigo_sala,capacidad,soporte,estado,fk_nombre)
VALUES
(101,250,'DI','D','Cine Woolands-Sense'),
(102,150,'3D','O','Cine Woolands-Sense'),
(201,500,'3D','D','Cine Woolands-Golden'),
(202,250,'3D','D','Cine Woolands-Golden'),
(203,500,'3D','O','Cine Woolands-Golden'),
(204,350,'DI','D','Cine Woolands-Golden'),
(301,300,'DI','D','Cine Woolands-Multiplex'),
(302,400,'DI','D','Cine Woolands-Multiplex'),
(303,250,'3D','D','Cine Woolands-Multiplex'),
(401,250,'DI','O','Cine Woolands-Stellar'),
(402,400,'3D','D','Cine Woolands-Stellar'),
(403,250,'DI','D','Cine Woolands-Stellar');

INSERT INTO contenido(codigo_contenido,clasificacion,pais,titulo,genero,duracion,idioma,fecha_estreno,tipo,director,sinopsis)
VALUES
(1,'B','Polonia','CORPUS CHRISTI','Drama','01:56:00','Polaco','2020-05-14',0,'Jan Komasa','Daniel experimenta una transformación espiritual mientras vive en un centro de detención juvenil. Quiere ser sacerdote, pero esto es imposible debido a sus antecedentes penales. Cuando es enviado a trabajar a un taller de carpintería en una pequeña ciudad, a su llegada se viste de sacerdote y se hace cargo accidentalmente de la parroquia local. La llegada del joven y carismático predicador es una oportunidad para que la comunidad local comience el proceso de sanación después de una tragedia que ocurrió allí.'),
(2,'C','España','MALASAÑA 32','Terror','01:30:00','Español','2020-05-14',0,' Albert Pintó','Manolo y Candela se instalan en el barrio de Malasaña, junto a sus tres hijos y el abuelo Fermín; buscando prosperidad que parece ofrecerles la capital de un país que se encuentra en plena transición política. Pero hay algo que la familia Olmedo no sabe: en la casa que han comprado, no están solos…'),
(3,'AA','Alemania','TABALUGA','Animación,Familiar','01:30:00','Alemán','2020-06-04',0,'Sven Unterwaldt Jr.','El joven y adorable dragón Tabaluga no sabe escupir fuego, así que intenta aprender. Un día, el siniestro Arktos le convence para viajar hasta su reino, en el hielo. Allí Tabaluga conoce a Lilli, la princesa de hielo. ¿Su amor lo ayudará a liberar por fin sus llamas?'),
(4,'D','Estados Unidos','SPIRAL: FROM THE BOOK OF SAW','Crimen,Horror','01:32:00','Inglés','2020-06-11',0,' Darren Lynn Bousman','Un cruel y sádico genio desata una retorcida forma de justicia en ESPIRAL, el nuevo y aterrador capítulo en el universo de El Juego del Miedo. A la sombra de un respetado veterano de la policía (Samuel L. Jackson), el atrevido detective Banks (Chris Rock) y su compañero novato (Max Minghella) se encargan de la investigación sobre unos terribles asesinatos que despiertan el recuerdo inquietante del escabroso pasado de la ciudad: ¿habrá regresado? ¿Será posible? Con cada movida, Banks se acerca más al centro del misterio y a los macabros juegos de un asesino.'),
(5,'B15','Reino Unido','REDCON-1','Terror','01:55:00','Inglés','2020-05-07',0,'Chee Keong Cheung','Un grupo de soldados combaten a sedientos zombies que están destruyendo londres con el objetivo de rescatar a un científico que tiene la cura de un virus letal.'),
(6,'A','Estados Unidos','GHOSTBUSTERS: AFTERLIFE','Aventura,Comedia','01:55:00','Inglés','2020-08-13',0,' Jason Reitman','Del director Jason Reitman y el productor Ivan Reitman, llega el próximo capítulo del universo original de Los Cazafantasmas. En Ghostbusters: El Legado, una madre soltera y sus dos hijos llegan a un pequeño pueblo y comienzan a descubrir su conexión con los cazafantasmas originales y el legado secreto que dejó su abuelo. La película está escrita por Jason Reitman y Gil Kenan.'),
(7,'AA','Estados Unidos',' THE SPONGEBOB MOVIE: SPONGE ON THE RUN','Animación,Aventura','01:44:00','Inglés','2020-05-28',0,'Tim Hill','Bob Esponja Pantalones Cuadrados, su mejor amigo Patricio Estrella y el resto de la pandilla de Fondo de Bikini, llegan a la pantalla grande en Bob Esponja: Al Rescate. Después de que la amada mascota de Bob Esponja, Gary el Caracol fuera secuescaracolada, él y Patricio se embarcan en una aventura épica hacia La Ciudad Pérdida de Atlantic City para regresar a Gary a casa. Mientras navegan por los deleites y peligros de esta hilarante misión de rescate, Bob Esponja y sus amigos prueban que no hay nada más fuerte que el poder de la amistad. '),
(8,'B','Australia/USA','INVISIBLE MAN','Suspenso','02:04:00','Inglés','2020-02-27',0,'Leigh Whannell','Lo que no puedes ver, puede hacerte daño.'),
(9,'A','Estados Unidos','SONIC THE HEDGEHOG','Animación,Acción','01:40:00','Inglés','2020-02-13',0,'Jeff Fowler','Basado en la exitosa franquicia de viodejuegos de SEGA.'),
(10,'A','Colombia','CONFERENCIA COVID-19','Investigación','02:00:00','Español','2020-03-01',1,null,null),
(11,'A','Estados Unidos','Big Hero 6','Animación,Aventuras','01:30:00','Inglés','2014-11-07',0,' Don Hall','Cuando un giro inesperado de eventos los sumerge en el medio de un peligroso plan, un niño prodigio, su robot y sus amigos se convierten en héroes de alta tecnología en una misión para salvar su ciudad.')
;


INSERT INTO proyecta(fecha,hora_inicio,hora_fin,fk_codigo_sala,fk_codigo_contenido)
VALUES
('2020-03-01','06:00:00','08:30:00',102,8),
('2020-03-01','04:00:00','06:00:00',203,9),
('2020-03-01','02:00:00','04:00:00',401,10);


INSERT INTO persona(identificacion,fecha_nac,edad,celular,email,direccion,nombres,apellidos,contraseña)
VALUES
('1007414346','1990-05-08',29, 3015765434,'p.ramirezg@gmail.com','Bucaramanga','Pedro', 'Ramirez Galvis','1239058409'),
('64568942','2000-12-05',19, 3166787654, 'martisep@yahoo.es','Bucaramanga','Martina', 'Sepúlveda Ojeda','contraseña1'),
('56784235','1990-12-06',28, 3015676432, 'fernandisortiz@hotmail.es', 'Bucaramanga','Fernanda ', 'Caceres Ortiz','osito'),
('976358087','1991-09-09',27, 6507646532, 'barryallen@hotmail.com','Los Angeles','Barry','James Allen','crack' ),
('1098765798','1984-06-03', 35, 2343565777, 'stepamellg@yahoo.es',null,'Stephen ','Amell Gustin','wtfman'),
('1345790224','1997-06-04', 22, 4565435467,  'pamelab@gmail.com',null,'Pamela', 'Baker Lotz','elmejordetodos'),
('47896422','1989-12-31', 29, 3445049545, 'patrigonz@hotmail.com','Bucaramanga','Patricio', 'Estupiñan Gonzalez','lasaqueadora3' ),
('56788754','1982-01-30',37,3434235932,'karejaimes@gmail.com','Bucaramanga', 'Karen Andrea', 'Jaimes Jaimes','nosequeponer' ),
('36789865','1980-06-05',39, 7678976568, 'tommydcsp@gmail.es', 'Chicago','Thomas', 'Donell Spencer','yacasiii'),
('63368846','2010-01-07',10, 6567898767,  'andrewmry@yahoo.es', null,'Andrew', 'Newball Merlyn','faltan3mas'),
('91245373','1970-05-08',49, 3019294949,'gloriamarce@gmail.com','Bucaramanga','Gloria Marcela', 'Santander Florez','parayaestarde'),
('27832910','1953-12-04',65,3214565432,'claudiapatri@gmail.com','Bucaramanga','Claudia Patricia', 'Alvarez Mayorga','thelastofus'),
('0000000000','0000-01-01',100,1111111111,'admin@proyecto.com','Bucaramanga','Admin','Admin','admin');


INSERT INTO empleado(identificacion,fecha_inicio,cargo,salario,fk_nombre)
VALUES
('976358087','2019-12-01','Taquillero',1200000,'Cine Woolands-Sense'),
('56788754','2019-12-01','Personal',1400000,'Cine Woolands-Golden'),
('47896422','2019-12-01','Taquillero',1200000,'Cine Woolands-Multiplex'),
('1098765798','2019-12-01','Mantenimiento',1800000,'Cine Woolands-Stellar'),
('0000000000','0000-01-01','Administrador',0,'Cine');

INSERT INTO cliente(identificacion,cod_tarjeta,saldo)
VALUES
('1007414346',1832,20000),
('64568942',1232,50000),
('1345790224',4453,200000),
('56788754',4536,60000),
('91245373',7567,80000),
('36789865',7857,90000);


INSERT INTO opinion(fecha,comentario,edad,calificacion,fk_codigo_contenido)
VALUES
('2020-03-01','excelente',29,5.0,8),
('2020-03-01','genial',19,4.8,8),
('2020-03-01','normal',22,4.0,8),
('2020-03-01','buena',37,4.5,9),
('2020-03-01','regular',49,3.0,9);

INSERT INTO recarga(valor,fecha_hora,fk_identificacion)
VALUES
(10000,'2020-02-28 12:21:00','1007414346'),
(20000,'2020-03-01 10:22:00','64568942'),
(100000,'2020-02-25 2:34:00','1345790224'),
(60000,'2020-02-26 11:36:00','56788754'),
(20000,'2020-02-27 10:01:00','91245373');

INSERT INTO promociones(cod_prom, nombre_prom,valor_desc,descrip_prom)
VALUES
(1, 'Navidad', 15,'Por ser navidad obtienes un super descuento'),
(2, 'Día de las madres', 25,'Disfruta este día con una gran película'),
(3, 'Cumpleaños', 30,'Por tus cumpleaños tendrás un descuento especial'),
(4, 'Cliente Preferido', 10,'Por ser uno de nuestros clientes preferidos'),
(5, 'Ninguna', 0,'Sin promoción');

INSERT INTO compra(cant_com, total,fecha_com,fk_identificacion,fk_codigo_comida)
VALUES
(1,13900,'2020-03-01','1007414346',201),
(1,5400,'2020-03-01','1007414346',403),
(2,66400,'2020-03-01','1345790224',103),
(2,13800,'2020-03-01','1345790224',504),
(1,8200,'2020-03-01','91245373',301),
(1,6200,'2020-03-01','91245373',402);

INSERT INTO visualiza(fecha_hora,cantidad,total,fk_identificacion,fk_codigo_proyecta,fk_cod_prom)
VALUES
('2020-03-01 06:00:00',1,29300,'1007414346',1,5),
('2020-03-01 06:00:00',1,10000,'64568942',2,5),
('2020-03-01 06:00:00',1,81200,'1345790224',2,4),
('2020-03-01 04:00:00',1,10000,'56788754',3,5),
('2020-03-01 04:00:00',1,24400,'91245373',3,5),
('2020-03-01 02:00:00',1,10000,'36789865',1,5);


