# API Contract - User Profile

**Endpoint:** `/api/v1/profile`  
**Method:** `GET`

**Response Body (JSON):**

```json
{
  "id": 1,
  "username": "mahasiswa_sd",
  "email": "mhs@univ.ac.id",
  "avatar_url": "https://image.com/avatar.png"
}
```

## Endpoint Login

**Endpoint:** `/api/v1/login`  
**Method:** `POST`

**Request Body (JSON):**

```json
{
  "email": "mhs@univ.ac.id",
  "password": "password123"
}
```

**Response Body (JSON):**

```json
{
  "success": true,
  "message": "Login berhasil",
  "token": "jwt_token_example"
}
```