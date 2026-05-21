# Estructuras de Datos - Dataset de Twitter con Índice Invertido

Este proyecto implementa índices invertidos sobre memoria dinámica.

## Dataset: Twitter MBTI Personality Types

Se utiliza un dataset real extraído de Twitter que contiene:

- **Perfiles de Usuario:** Identificación única y metadatos.
- **Posts:** Contenido textual original de los tweets.
- **Seguidores:** Qué usuario sigue a qué usuario.

Debido a que el dataset carece de lo siguiente, estos datos serán generados de forma sintética:

- **Registro de Likes:** Registro de likes dados por usuarios.

### Procesamiento de Datos

- **Reducción de filas:** Ya que el dataset cuenta con al rededor de 10.000 usuarios, los datos se han reducido a 100 filas para probar el código `data/test_data/` y 1500 filas para la ejecución final `data/less_data/`.
- **Reducción de posts** cada usuario tiene ahora un máximo de 50 posts (en el dataset original son 200).
- **Preprocesamiento de amigos:** Se ha generado una tabla `friends.csv` a partir de la tabla `edges.csv` para facilitar la consulta de amigos de cada usuario.
- **Creación sintética de Likes:** Ya que nuestro dataset carece de información sobre los likes que ha dado cada usuario a distintos posts nosotros creamos esos datos de forma sintética y aleatoria, utilizando la información de los demás archivos CSV en `likes.csv`.

## Diagramas de las estructuras de datos creadas

```mermaid
classDiagram
    class Usuario {
        usuario_id: str
        nombre: str
        descripción: str
        número_de_seguidores: int
        amigos: LinkedList
    }
```

```mermaid
graph LR
    subgraph D["Diccionario (claves)"]
        K1["'Usuario A'"]
        K2["'Usuario B'"]
        K3["'Usuario C'"]
    end

    subgraph L["Listas Enlazadas de Nodos de Amigos (valores)"]
        K1 --> NodeA1["Usuario 1 (Amigo)"]
        NodeA1 --> NodeA2["Usuario 2 (Amigo)"]
        NodeA2 --> NodeA3["Usuario 3 (Amigo)"]
        NodeA3 --> Null1((null))

        K2 --> NodeB1["Usuario 4 (Amigo)"]
        NodeB1 --> Null2((null))

        K3 --> NodeC1["Usuario 5 (Amigo)"]
        NodeC1 --> NodeC2["Usuario 6 (Amigo)"]
        NodeC2 --> Null3((null))
    end
```

```mermaid
classDiagram
    class Post {
        post_id: str
        autor: str
        texto: str
        likes: LinkedList
    }
```

```mermaid
graph LR
    subgraph D["Diccionario (claves)"]
        T1['tecnología']
        T2['noticia']
        T3['programación']
    end

    subgraph L ["Listas Enlazadas de Nodos de Posts (Valores)"]
        T1 --> PostA1[Post 1]
        PostA1 --> PostA2[Post 2]
        PostA2 --> NullA((null))

        T2 --> PostB1[Post 3]
        PostB1 --> PostB2[Post 5]
        PostB2 --> PostB3[Post 7]
        PostB3 --> NullB((null))

        T3 --> PostC1[Post 1]
        PostC1 --> NullC((null))
    end
```

## Como ejecutar el proyecto

### pre-requisitos:

- Git
- Python
- [Poetry](https://python-poetry.org/docs/) (administrador de dependencias de python)

### paso a paso:

```bash
# clonar repo
git clone https://github.com/College-Homework-Repos/tarea1-estructura-de-datos-twitter-dataset.git
cd tarea1-estructura-de-datos-twitter-dataset

# instalar dependencias
poetry install

# preprocesar los datos
# descargar dataset, generar tablas y reducir filas.
poetry run python ./preprocessing/main.py

# ejecutar el proyecto
poetry run python ./src/main.py
```
