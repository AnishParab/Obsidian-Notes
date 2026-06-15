# Spatial Datatypes

- Used for geographical and geometric data.

| Datatype     | Description            |
| ------------ | ---------------------- |
| `POINT`      | Single coordinate      |
| `LINESTRING` | Sequence of points     |
| `POLYGON`    | Closed geometric shape |
| `GEOMETRY`   | Generic spatial value  |

**Example**
```sql
CREATE TABLE locations (
    id INT PRIMARY KEY,
    coordinates POINT
);
```

---
