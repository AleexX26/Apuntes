

'' Esto es una macro para poder generar facturas o cosas parecidas atraves de un menu desplegable que se descarga todo en PDF y se guarda en la carpeta indicada del ordenador.
'' Puede que sea necesario cambiar la linea 14 y 17 por las celdas corespondientes, solo cambiar el numero, EN TODO EL SCRIPT no solo en las lineas 14 y 17.


Sub GenerarFacturasPDF()
    Dim wsHoja As Worksheet
    Dim i As Long
    Dim carpetaDestino As String
    Dim NombreArchivo As String
    Dim rutaPDF As String
    Dim FSO As Object
    Dim valorO3 As String
    Dim itemCount As Long
    Dim validationRange As Range
    Dim valorO18 As String

    ' Asignar la hoja
    Set wsHoja = ThisWorkbook.Sheets("PONER_NOMBRE_DE_LA_HOJA")             '' -------------> COSA QUE MODIFICAR <-------------
    ' Carpeta de destino
    carpetaDestino = "UBICACION_DE_LA_CARPETA_DONDE_SE_GUARDA_LOS_DOCUMENTOS"             '' -------------> COSA QUE MODIFICAR <-------------

    ' Verificar si la carpeta existe, si no, crearla
    Set FSO = CreateObject("Scripting.FileSystemObject")
    If Not FSO.FolderExists(carpetaDestino) Then
        On Error Resume Next
        MkDir carpetaDestino
        If Err.Number <> 0 Then
            MsgBox "Error al crear la carpeta 'Intento facturas'. Verifique los permisos o el nombre de la carpeta.", vbCritical
            Exit Sub
        End If
        On Error GoTo 0
    End If

    ' Obtener el rango de valores del menú desplegable en O3
    Set validationRange = Evaluate(wsHoja.Range("O3").Validation.Formula1)

    ' Contar la cantidad de opciones en el menú desplegable
    itemCount = validationRange.Count

    ' Recorrer cada valor del menú desplegable
    For i = 1 To itemCount
        valorO3 = validationRange.Cells(i, 1).Value

        ' Actualizar el valor en la celda O3
        wsHoja.Range("O3").Value = valorO3

        ' Forzar la actualización de la hoja (por si O18 depende de otros valores)
        wsHoja.Calculate

        ' Obtener el valor actual de la celda O18
        valorO18 = wsHoja.Range("O18").Value

        ' Verificar si O18 tiene un valor
        If Trim(valorO18) = "" Then
            MsgBox "La celda O18 está vacía. No se puede generar el archivo PDF.", vbCritical
            Exit Sub
        End If

        ' Definir el área de impresión
        wsHoja.PageSetup.PrintArea = wsHoja.Range("B2:J54").Address

        ' Nombre del archivo PDF usando el valor en O18
        NombreArchivo = "Factura_" & valorO18 & ".pdf"

        ' Ruta completa del archivo PDF
        rutaPDF = carpetaDestino & "\" & NombreArchivo

        ' Mostrar la ruta para depuración
        Debug.Print "Exportando: " & rutaPDF

        ' Intentar exportar la hoja "Factura" como PDF
        On Error Resume Next
        wsHoja.ExportAsFixedFormat Type:=xlTypePDF, Filename:=rutaPDF, Quality:=xlQualityStandard, _ IncludeDocProperties:=True, IgnorePrintAreas:=False, OpenAfterPublish:=False
        If Err.Number <> 0 Then
            MsgBox "Error al exportar el archivo PDF: " & Err.Description, vbCritical
            Err.Clear
        End If
        On Error GoTo 0
    Next i

    ' Mensaje de finalización
    MsgBox "Facturas generadas y guardadas en PDF correctamente.", vbInformation
End Sub