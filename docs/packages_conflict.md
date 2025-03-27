# 🛠 Fixing `bson.objectid` Import Error in PyMongo

## ❌ Error Message
```sh
(flask-app) workstation@Nana-Kwasi-Fosu:/mnt/d/Flask API$ python -c "import pymongo; from bson import ObjectId; print('✅ PyMongo and BSON are working')"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/mnt/d/Flask API/flask-app/lib/python3.12/site-packages/pymongo/__init__.py", line 90, in <module>
    from pymongo.collection import ReturnDocument
  File "/mnt/d/Flask API/flask-app/lib/python3.12/site-packages/pymongo/collection.py", line 39, in <module>
    from bson.objectid import ObjectId
ModuleNotFoundError: No module named 'bson.objectid'
```

## ✅ Solution Steps

### 1️⃣ **Completely Remove `bson` and `pymongo`**
Since `bson` was manually installed, it likely broke `pymongo`. Let's remove them:
```sh
pip uninstall bson pymongo
```
👉 Run this command multiple times if needed until both are fully removed.

---
### 2️⃣ **Clear Pip Cache**
To prevent installing broken or cached versions:
```sh
pip cache purge
```

---
### 3️⃣ **Reinstall `pymongo` Without `bson`**
Now, install `pymongo` correctly without manually installing `bson`:
```sh
pip install --no-cache-dir pymongo
```
This will install the correct version of `bson` bundled inside `pymongo`.

---
### 4️⃣ **Verify the Fix**
Run this command again to check if everything is working:
```sh
python -c "import pymongo; from bson import ObjectId; print('✅ PyMongo and BSON are working')"
```
✅ **Expected Output:**
```sh
✅ PyMongo and BSON are working
```
If you see this message, the issue is fixed!

---
### 5️⃣ **Run Your Flask App Again**
Finally, restart your application:
```sh
python run.py
```

---
## 🛠 **Why This Happens?**
- The `bson` package **should not** be installed separately.
- `pymongo` already **includes** the correct `bson` module.
- Installing `bson` manually causes **conflicts** because it overrides the correct version inside `pymongo`.

This should fix your issue! 🚀

