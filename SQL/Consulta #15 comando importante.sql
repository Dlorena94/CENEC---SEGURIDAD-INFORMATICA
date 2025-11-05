SELECT*
FROM vehiculos
WHERE(combustible = 'Híbrido' OR combustible ='Gasolina')
AND matriculacion BETWEEN 2017 AND 2019
AND kilometros> 50000
AND id_marca NOT IN (9, 11, 13);
