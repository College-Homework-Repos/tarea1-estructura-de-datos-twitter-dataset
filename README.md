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
- Los datos son preprocesados para descartar columnas no usadas y crear las tablas estrictamente necesarias.
- **Filtrado de Stop Words:** Eliminación de artículos, preposiciones y conectores (e.g., "el", "la", "y", "en").
- **Creación sintética de datos:** Ya que nuestro dataset carece de información sobre los likes que ha dado cada usuario a distintos posts nosotros creamos esos datos de forma sintética y aleatoria, utilizando la información de los demás archivos CSV.

### Diagramas de las estructuras de datos creadas
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

```mermaid
graph LR
    subgraph D["Diccionario (claves)"]
        K1["'Usuario A'"]
        K2["'Usuario B'"]
        K3["'Usuario C'"]
    end

    subgraph L["Listas Enlazadas de Nodos de Amigos (valores)"]
        K1 --> NodeA1[Amigo 1]
        NodeA1 --> NodeA2[Amigo 2]
        NodeA2 --> NodeA3[Amigo 3]
        NodeA3 --> Null1((null))

        K2 --> NodeB1[Amigo 4]
        NodeB1 --> Null2((null))

        K3 --> NodeC1[Amigo 5]
        NodeC1 --> NodeC2[Amigo 6]
        NodeC2 --> Null3((null))
    end
```

## Estructura del Repositorio
```text
- raw-data/         # Archivos CSV sin procesar del dataset
- data/             # Archivos CSV procesados del dataset
- src/              # Código fuente en Python
- preprocessing/    # Script Python para preprocesar datos CSV
```
