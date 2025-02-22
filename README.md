# Morphe-OA

This project is a **Django-based web application** deployed on **GitHub Codespaces** with a `/htop` endpoint that displays system information, including:
- **Name**: Ankit Rajpoot
- **Server Time**: Displayed in IST
- **Top Output**: The top 10 processes running on the server

---

## 🚀 Setup & Deployment

### 1️⃣ **Setup GitHub Codespace**
1. Go to **[GitHub Codespaces](https://github.com/codespaces)**.
2. Create a new codespace for this repository.
3. Set timeout to **240 minutes (maximum)**.

### 2️⃣ **Install Dependencies**
Run the following command in the Codespace terminal:
```bash
pip install django
```

### 3️⃣ **Run the Project**
```bash
python manage.py runserver 0.0.0.0:8000
```

### 4️⃣ **Expose Port**
- Go to **PORTS** in Codespaces.
- **Make port 8000 public** to allow external access.

---

## 📌 API Endpoint

### **`/htop` Endpoint**
This endpoint provides system information in a structured format.

#### ✅ Example Response:
```
<h1>System Info</h1>
<p><strong>Name:</strong> Ankit Rajpoot</p>
<p><strong>Username:</strong> codespaces-user</p>
<p><strong>Server Time (IST):</strong> 2025-02-22 14:30:00 IST</p>
<pre>
PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
1   root      20   0  225272   8856   6984 S   0.0  0.1   0:01.23 systemd
...
</pre>
```

---

## 🛠️ Project Structure
```
Morphe-OA/
├── myapp/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
├── htop_app/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── admin.py
│   └── ...
└── manage.py
```



