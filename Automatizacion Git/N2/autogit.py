from os import system as s
from os import chdir as c

print('AUTOMATIZACION GIT'
      '\n'
      '\n\t[1] Actualizar Repositorios'
      '\n\t[2] Subir Cambios'
      '\n')
opcion = int(input('Selecciona una opcion: '))

if opcion == 1:
    c('D:\Archivos\[Git] Progra Avanzada (N2)\contenidos')
    s('git pull')

    c('D:\Archivos\[Git] Progra Avanzada (N2)\RickyUC-iic2233-2017-1')
    s('git pull')

    c('D:\Archivos\[Git] Progra Avanzada (N2)\Syllabus')
    s('git pull')

    c('D:\Archivos\[Git] Progra Avanzada (N2)\Programas')
    s('git pull')

elif opcion == 2:
    print('ADVERTENCIA: \nEste programa carga todos los archivos del repositorio RickyUC-iic2233-2017-1 sin discriminar'
          'bajo ninguna categoria.')
    continuar = int(input('¿Deseas continuar? si[1]/no[2] '))

    if continuar == 1:
        c('D:\Archivos\[Git] Progra Avanzada (N1)\RickyUC-iic2233-2017-1')
        s('git add --all')
        comentario = str(input('Insertar comentario de cambios: '))
        s('git commit -m ' + '"' + comentario + '"')
        s('git push')
