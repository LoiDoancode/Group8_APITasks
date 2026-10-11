Nhóm 8 - Lớp học phần: INT3505E 1

**Thành viên:**
* Doãn Duy Lợi - MSV: 24021549
* Nguyễn Phúc Thành - MSV: 
* An Đức Minh Trí - MSV: 
* Hoàng Lâm Tùng - MSV: 
* Nguyễn Xuân Tường - MSV:
  
```text
Group8_APITasks/
├── README.md                          # Tài liệu giới thiệu & hướng dẫn chạy dự án
├── package.json                       # Cấu hình kiểm thử Redocly / Prism CLI
└── task-api/
    ├── openAPI.yaml                   # [FILE GỐC ĐIỀU PHỐI] Root OpenAPI Specification 3.0.3
    ├── app.py                         # Server Python Flask cung cấp Swagger UI trực quan
    ├── plan.md                        # Kế hoạch phân công và quy chuẩn kỹ thuật
    ├── paths/                         # Endpoints chia theo module
    │   ├── auth.yaml                  # Xác thực (Đăng nhập, Đăng ký, Lấy thông tin cá nhân)
    │   ├── books.yaml                 # Quản lý Sách (Truy vấn phân trang, Chi tiết, Thêm/Sửa/Xóa)
    │   ├── authors.yaml               # Quản lý Tác giả (Danh sách phân trang, Chi tiết, Thêm/Sửa/Xóa)
    │   └── borrows.yaml (borrow.yaml) # Quy trình Mượn & Trả sách (Lập phiếu, Gia hạn, Trả, Hủy)
    └── components/                    # Tài nguyên tái sử dụng
        ├── schemas.yaml               # Dữ liệu Model & DTO (Book, Author, Borrow, User, Error...)
        └── responses.yaml             # Chuẩn hóa mã phản hồi HTTP lỗi (400, 401, 403, 404, 500)
```
