<?php
/* Agrega conexion a la base de datos*/
require_once "../config/database.php";

// datos enviados desde el formulario de inicio de sesion
$username = mysqli_real_escape_string($mysqli, stripslashes(strip_tags(htmlspecialchars(trim($_POST['username'])))));
$password = mysqli_real_escape_string($mysqli, stripslashes(strip_tags(htmlspecialchars(trim($_POST['password'])))));
// asegúrese de que el nombre de usuario y la contraseña es en forma de letras o números.


	// comprobación de los datos
	$query = mysqli_query($mysqli, "SELECT * FROM colegio_alumno WHERE alumno_email='$username' AND alumno_ident='$password'")
									or die('Error: '.mysqli_error($mysqli));
	$rows  = mysqli_num_rows($query);
	$query2 = mysqli_query($mysqli, "SELECT * FROM colegio_profesor WHERE profesor_email='$username' AND profesor_ident='$password'")
									or die('Error: '.mysqli_error($mysqli));
	$rows2  = mysqli_num_rows($query2);

	// Si los datos estan correctos, entonces inicio sesion
	if ($rows2 > 0) {
		$data  = mysqli_fetch_assoc($query2);

		session_start();
		$_SESSION['ident'] = $data['profesor_ident'];
		$_SESSION['nombres'] = $data['profesor_nombres'];
		$_SESSION['apellidos'] = $data['profesor_apellidos'];
		$_SESSION['email'] = $data['profesor_email'];
		$_SESSION['type'] = "profesor";
		// Redirecciona a la pagina principal
		header("Location: index3.php?module=home");
		exit();
	}

	if ($rows > 0) {
		$data  = mysqli_fetch_assoc($query);

		session_start();
		$_SESSION['ident'] = $data['alumno_ident'];
		$_SESSION['nombres'] = $data['alumno_nombres'];
		$_SESSION['apellidos'] = $data['alumno_apellidos'];
		$_SESSION['email'] = $data['alumno_email'];
		$_SESSION['curso'] = $data['codigo_curso'];
		$_SESSION['type'] = "alumno";
		// Redirecciona a la pagina principal
		header("Location: index3.php?module=home");
		exit();
	}

	// Sino existen los datos entonces envio de nuevo al login mostrando un error alert=1
	else {
		header("Location: index.php?alert=1");
	}

?>