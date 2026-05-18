# Database Schema

## Tabel Users

Digunakan untuk menyimpan data pengguna aplikasi.

Kolom:
- id
- username
- email
- password
- avatar_url
- created_at

---

## Tabel Posts

Digunakan untuk menyimpan postingan pengguna.

Kolom:
- id
- user_id
- title
- content
- created_at

---

## Tabel Comments

Digunakan untuk menyimpan komentar pada postingan.

Kolom:
- id
- post_id
- user_id
- comment
- created_at