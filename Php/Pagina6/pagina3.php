<?php
session_start();
?>
<html>
    <head>
        <title></title>
    </head>
    <body>
        <?php
            if($_SESSION['numeroaleatorio'] == $_REQUEST['numero']){
                echo "Correcto";
            } else{
                echo "Incorrecto";
            }
            ?>
    </body>
</html>