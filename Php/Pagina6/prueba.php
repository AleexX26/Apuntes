<html>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <?php
    $nombre = "Pol";
    $hora = date("d/m/y");
    if ($hora >= 8 && $hora <= 14)
        $saludo = " Buenas dias, ";
    else if ($hora > 14 && $hora <= 20)
        $saludo = "Buenas Tardes, ";
    else
        $saludo = "Buenas noches, ";
    $saludo1 = $saludo . $nombre;
    print("$saludo1 ");
    print("$hora");
    ?>
</body>
</html>