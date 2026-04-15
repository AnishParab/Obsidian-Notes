# View of Data (Three Schema Architecture)

> The main objective of three level architecture is to enable multiple users to access the same data with a personalized view while storing the underlying data only once.

![[three_schema_architecture_dbms.excalidraw|700]]

---
# Physical level / Internal level

- The lowest level of abstraction describes how the data is stored.
- Low-level data structures used.
- It has **Physical Schema** which describes how the data are stored.
- Talks about: Storage allocation (N-ary tree etc), Data compression and encryption etc.
- **Goal**: We must define algorithms that allow efficient access to data.

---
# Logical level / Conceptual level

- The **conceptual schema** describes the design of a database at the conceptual level, describes **what** data are stored in DB, and what **relationships** exist among those data.
- User at logical level does not need to be aware about physical-level structures.
- **DBA**, who must decide what information to keep in the DB use the logical level of abstraction.
- **Goal**: ease to use.

---
# View level / External level

- Highest level of abstraction aims to simplify user interactions with the system by providing different view to different end-user.
- Each **view schema** describes the database part that a particular user group is interested and hides the remaining database from that user group.
- At the external level, a database contains several schemas thats sometimes called as **subschema**. The subschema is used to describe the different view of the database.
- At views also provide a **security** mechanism to prevent users from accessing certain parts of DB.

---
