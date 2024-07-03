import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def realizar_regresion(data):
    try:
        df = pd.DataFrame(data, columns=['x', 'y'])
        df = df.apply(pd.to_numeric, errors='coerce')

        if df.isnull().values.any():
            raise ValueError("Los datos contienen valores no numéricos o NaN.")
        
        X = df['x'].values.reshape(-1, 1)
        y = df['y'].values

        if len(X) < 2 or len(y) < 2:
            raise ValueError("Se requieren al menos dos puntos de datos para realizar la regresión.")

        # Calcular valores adicionales
        df['x*y'] = round(df['x'] * df['y'], 3)
        df['x^2'] = round(df['x'] ** 2, 3)
        df['y^2'] = round(df['y'] ** 2, 3)

        suma_x = round(df['x'].sum().item(), 3)
        suma_y = round(df['y'].sum().item(), 3)
        suma_xy = round(df['x*y'].sum().item(), 3)
        suma_x2 = round(df['x^2'].sum().item(), 3)
        suma_y2 = round(df['y^2'].sum().item(), 3)

        model = LinearRegression()
        model.fit(X, y)

        r_cuadrado = model.score(X, y)
        intercepcion = model.intercept_
        pendiente = model.coef_.tolist()
        r = np.corrcoef(df['x'], df['y'])[0, 1]
        y_pred = model.predict(X)
        syx = np.sqrt(np.mean((y - y_pred) ** 2))

        ecuacion = f'Y = {round(pendiente[0], 3)}x + {round(intercepcion, 3)}'

        result = {
            'r': r,
            'r_cuadrado': r_cuadrado,
            'pendiente': pendiente[0],
            'intercepcion': intercepcion,
            'syx': syx,
            'ecuacion': ecuacion,
            'valores': df.to_dict(orient='records'),
            'suma_x': suma_x,
            'suma_y': suma_y,
            'suma_xy': suma_xy,
            'suma_x2': suma_x2,
            'suma_y2': suma_y2
        }
        
        return result

    except Exception as e:
        raise ValueError("Error en la función realizar_regresion: " + str(e))
