<?php

session_start();
?>
<html>

<head>
    <title>Problema</title>
</head>

<body>
    <?php
    if ($SESSION['numeroaleatorio'] == $REQUEST['numero']) {
        echo "Ingreso el valor correcto";
    } else {
        echo "Incorrecto";
    }
    ?>
</body>

</html>