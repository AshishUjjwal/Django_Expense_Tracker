# Django ORM Queries

Django's Object-Relational Mapper (ORM) allows you to interact with the database using Python instead of writing raw SQL queries. This makes development faster and more secure.

---

## 1️⃣ Fetching Data (SELECT Queries)

### Get all records
```python
users = User.objects.all()
```
**SQL Equivalent:**
```sql
SELECT * FROM auth_user;
```

### Get a single record (filter by ID)
```python
user = User.objects.get(id=1)
```
**SQL Equivalent:**
```sql
SELECT * FROM auth_user WHERE id = 1;
```

### Filter records (WHERE clause)
```python
users = User.objects.filter(is_active=True)
```
**SQL Equivalent:**
```sql
SELECT * FROM auth_user WHERE is_active = TRUE;
```

### Filter with multiple conditions (AND & OR)
```python
users = User.objects.filter(is_active=True, email__contains="gmail")
```
**SQL Equivalent:**
```sql
SELECT * FROM auth_user WHERE is_active = TRUE AND email LIKE '%gmail%';
```

For OR conditions, use `Q`:
```python
from django.db.models import Q

users = User.objects.filter(Q(is_active=True) | Q(email__contains="gmail"))
```
**SQL Equivalent:**
```sql
SELECT * FROM auth_user WHERE is_active = TRUE OR email LIKE '%gmail%';
```

---

## 2️⃣ Creating Data (INSERT Query)

### Create a new user
```python
user = User.objects.create(username="john_doe", email="john@example.com", is_active=True)
```
**SQL Equivalent:**
```sql
INSERT INTO auth_user (username, email, is_active) VALUES ('john_doe', 'john@example.com', TRUE);
```

### Another way: Using `.save()`
```python
user = User(username="john_doe", email="john@example.com", is_active=True)
user.save()
```

---

## 3️⃣ Updating Data (UPDATE Query)

### Update a single field
```python
user = User.objects.get(id=1)
user.is_active = False
user.save()
```
**SQL Equivalent:**
```sql
UPDATE auth_user SET is_active = FALSE WHERE id = 1;
```

### Update multiple records
```python
User.objects.filter(is_active=True).update(is_active=False)
```
**SQL Equivalent:**
```sql
UPDATE auth_user SET is_active = FALSE WHERE is_active = TRUE;
```

---

## 4️⃣ Deleting Data (DELETE Query)

### Delete a single record
```python
user = User.objects.get(id=1)
user.delete()
```
**SQL Equivalent:**
```sql
DELETE FROM auth_user WHERE id = 1;
```

### Delete multiple records
```python
User.objects.filter(is_active=False).delete()
```
**SQL Equivalent:**
```sql
DELETE FROM auth_user WHERE is_active = FALSE;
```

---

## 5️⃣ Ordering & Limiting Data

### Order by a field
```python
users = User.objects.order_by('username')  # Ascending
users = User.objects.order_by('-username')  # Descending
```
**SQL Equivalent:**
```sql
SELECT * FROM auth_user ORDER BY username ASC;
SELECT * FROM auth_user ORDER BY username DESC;
```

### Limit results (LIKE SQL’s LIMIT)
```python
users = User.objects.all()[:5]  # Get first 5 users
```
**SQL Equivalent:**
```sql
SELECT * FROM auth_user LIMIT 5;
```

---

## 6️⃣ Aggregations & Count

### Count records
```python
user_count = User.objects.count()
```
**SQL Equivalent:**
```sql
SELECT COUNT(*) FROM auth_user;
```

### Sum, Avg, Max, Min
```python
from django.db.models import Sum, Avg, Max, Min

total_users = User.objects.aggregate(Sum('id'))
average_id = User.objects.aggregate(Avg('id'))
max_id = User.objects.aggregate(Max('id'))
```
**SQL Equivalent:**
```sql
SELECT SUM(id), AVG(id), MAX(id) FROM auth_user;
```

---

## 7️⃣ Using Raw SQL in Django
If you ever want to write raw SQL, you can do it like this:
```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM auth_user WHERE is_active = TRUE")
    rows = cursor.fetchall()
    print(rows)
```

---

## 🚀 Summary: Why Use Django ORM?
✅ No need to write raw SQL manually.  
✅ Prevents SQL Injection.  
✅ Makes querying **easier & readable**.  
✅ Works across **multiple databases** (PostgreSQL, MySQL, SQLite, etc.).  

---

Let me know if you need any modifications! 🚀

