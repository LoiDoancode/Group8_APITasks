# KẾ HOẠCH DỰ ÁN VÀ HƯỚNG DẪN THỰC HIỆN: OPENAPI QUẢN LÝ THƯ VIỆN SÁCH (TASK-API)
**Nhóm 8 - Lớp học phần: INT3505E 1 (Kiến trúc hướng dịch vụ)**

---

## I. TỔNG QUAN HỆ THỐNG VÀ CẤU TRÚC DỰ ÁN

Hệ thống được thiết kế theo chuẩn **OpenAPI Specification 3.0.3** với kiến trúc **Modular (chia nhỏ file)** giúp 5 thành viên làm việc song song độc lập, không gây xung đột (conflict) mã nguồn trên Git.

### 1. Cấu trúc cây thư mục
```text
Group8_APITasks/
├── README.md                          # Tài liệu giới thiệu dự án, thành viên, hướng dẫn chạy (TV5 phụ trách viết)
├── package.json                       # Khai báo cấu hình dự án (tùy chọn)
└── task-api/
    ├── openAI.yaml                    # [FILE GỐC ĐIỀU PHỐI] Root OpenAPI Specification
    ├── plan.md                        # [TÀI LIỆU NÀY] Hướng dẫn và phân công công việc
    ├── paths/                         # Thư mục chứa các API Endpoints
    │   ├── auth.yaml                  # Module Xác thực (TV1 & TV5 phụ trách)
    │   ├── books.yaml                 # Phần 1: Module Quản lý Sách (TV2 phụ trách trọn gói)
    │   ├── authors.yaml               # Phần 2: Module Quản lý Tác giả (TV3 phụ trách trọn gói)
    │   └── borrow.yaml                # Phần 3: Module Mượn/Trả sách (TV4 phụ trách trọn gói)
    └── components/                    # Thư mục tài nguyên dùng chung
        ├── schemas.yaml               # Định nghĩa Model/DTO (Book, Author, Borrow, User, Error...)
        └── responses.yaml             # Định nghĩa các mã lỗi HTTP chuẩn (400, 401, 403, 404, 500)
```

---

## II. BẢNG PHÂN| Thành viên | Phân hệ / Nhiệm vụ phụ trách | File làm việc chính |
| :--- | :--- | :--- |
| **Thành viên 1** *(Doãn Duy Lợi - Leader)* | Setup khung dự án, Root Spec, Auth APIs, Quản trị Git/PR | `openAI.yaml`, `paths/auth.yaml`, `components/` |
| **Thành viên 2** | **Phần 1 Paths:** Toàn bộ API Quản lý Sách (Query & CRUD) | `paths/books.yaml`, `components/schemas.yaml` |
| **Thành viên 3** | **Phần 2 Paths:** Toàn bộ API Quản lý Tác giả (Query & CRUD) | `paths/authors.yaml`, `components/schemas.yaml` |
| **Thành viên 4** | **Phần 3 Paths:** Toàn bộ API Quy trình Mượn & Trả sách | `paths/borrow.yaml`, `components/schemas.yaml` |
| **Thành viên 5** | Phối hợp cùng TV1 (Auth, Schemas/Responses, QA) + **Viết README.md** | `README.md`, `paths/auth.yaml`, `components/` |`, `components/` | ⏳ Đang thực hiện |

---

## III. NHIỆM VỤ CHI TIẾT CỦA TỪNG THÀNH VIÊN

---

### 👤 THÀNH VIÊN 1: Team Leader / DevOps & Core Architecture (Doãn Duy Lợi)
* **File phụ trách chính:**
  - `task-api/openAI.yaml`
  - `task-api/paths/auth.yaml`
  - Khung nền tảng trong `components/schemas.yaml` & `components/responses.yaml`
* **Công việc cụ thể:**
  1. **Khởi tạo hạ tầng dự án (`openAI.yaml`):**
     - Thiết lập chuẩn OpenAPI 3.0.3, thông tin liên hệ, server môi trường, danh sách `tags`.
     - Cấu hình bảo mật toàn cục **JWT Bearer Token** (`BearerAuth`).
     - Kết nối điều phối toàn bộ các file endpoints con qua `$ref`.
  2. **Viết Module Xác thực (`paths/auth.yaml`):**
     - `POST /auth/login`: Nhận username & password, cấp JWT Access Token.
     - `POST /auth/register`: Đăng ký tài khoản người dùng mới.
     - `GET /auth/me`: Lấy thông tin tài khoản hiện tại qua token.
  3. **Khởi tạo bộ khung Schemas/Responses dùng chung:**
     - Tạo sẵn cấu trúc lỗi `ErrorResponse`, `ErrorDetail`, `PaginationMeta` và mã lỗi HTTP 400, 401, 403, 404, 500.
     - Tạo khung sườn ban đầu cho `Book`, `Author`, `BorrowRecord` để các bạn không phải tạo từ đầu.

---

### 👤 THÀNH VIÊN 2: Module Quản lý Sách (Toàn diện Query & CRUD)
* **File phụ trách:**
  - `task-api/paths/books.yaml`
  - `task-api/components/schemas.yaml` (các schemas liên quan đến Book)
* **Công việc cụ thể cần làm:**
  1. **Viết các API Truy vấn sách:**
     - `GET /books`: Lấy danh sách sách có hỗ trợ phân trang (`page`, `limit`), tìm kiếm (`search`), lọc theo danh mục (`category`), tác giả (`author_id`). Trả về danh sách sách kèm `PaginationMeta`.
     - `GET /books/{id}`: Xem thông tin chi tiết một cuốn sách theo UUID. Trả về `Book` hoặc lỗi `404 NotFound`.
  2. **Viết các API Thao tác dữ liệu sách (CRUD):**
     - `POST /books`: Thêm sách mới vào thư viện (yêu cầu Bearer Token). RequestBody: `BookCreateInput`. Trả về `201 Created`.
     - `PUT /books/{id}`: Cập nhật thông tin sách (yêu cầu Bearer Token). RequestBody: `BookUpdateInput`. Trả về `200 OK`.
     - `DELETE /books/{id}`: Xóa sách khỏi thư viện (yêu cầu Bearer Token). Trả về `204 No Content`.
  3. **Hoàn thiện Schemas trong `schemas.yaml`:**
     - Chi tiết hóa `Book`, tạo mới `BookCreateInput`, `BookUpdateInput`.

---

### 👤 THÀNH VIÊN 3: Module Quản lý Tác giả (Toàn diện Query & CRUD)
* **File phụ trách:**
  - `task-api/paths/authors.yaml`
  - `task-api/components/schemas.yaml` (các schemas liên quan đến Author)
* **Công việc cụ thể cần làm:**
  1. **Viết các API Truy vấn tác giả:**
     - `GET /authors`: Lấy danh sách tác giả (có hỗ trợ phân trang `page`, `limit` và tìm kiếm theo tên `name`).
     - `GET /authors/{id}`: Xem chi tiết tiểu sử và thông tin của 1 tác giả theo ID.
  2. **Viết các API Thao tác dữ liệu tác giả (CRUD):**
     - `POST /authors`: Thêm tác giả mới (yêu cầu Bearer Token). RequestBody: `AuthorCreateInput`. Trả về `201 Created`.
     - `PUT /authors/{id}`: Sửa đổi thông tin tác giả (yêu cầu Bearer Token).
     - `DELETE /authors/{id}`: Xóa tác giả khỏi hệ thống (yêu cầu Bearer Token).
  3. **Hoàn thiện Schemas trong `schemas.yaml`:**
     - Bổ sung chi tiết cho schema `Author`, tạo thêm `AuthorCreateInput` (`name`, `email`, `bio`, `birth_date`).

---

### 👤 THÀNH VIÊN 4: Module Mượn / Trả Sách (Borrow Process)
* **File phụ trách:**
  - `task-api/paths/borrow.yaml`
  - `task-api/components/schemas.yaml` (các schemas liên quan đến Borrow)
* **Công việc cụ thể cần làm:**
  1. **Viết các API Quy trình mượn & trả:**
     - `POST /borrow`: Tạo phiếu mượn sách mới (yêu cầu Bearer Token). RequestBody: `BorrowCreateInput` (chứa `book_id`, `borrow_days`). Trả về `201 Created`.
     - `GET /borrow`: Lấy danh sách lịch sử các phiếu mượn (của người dùng hiện tại hoặc toàn bộ nếu là thủ thư).
     - `GET /borrow/{id}`: Xem chi tiết thông tin 1 phiếu mượn (sách nào, người mượn, hạn trả).
     - `PUT /borrow/{id}/return`: Thực hiện trả sách, cập nhật trạng thái phiếu từ `borrowed` sang `returned`, ghi nhận ngày trả thực tế.
  2. **Hoàn thiện Schemas trong `schemas.yaml`:**
     - Hoàn thiện schema `BorrowRecord` và tạo mới `BorrowCreateInput`.

---

### 👤 THÀNH VIÊN 5: Đồng hành cùng TV1 (Auth, Common Schemas, QA) & Phụ trách README.md
* **File phụ trách chính:**
  - [`README.md`](file:///c:/game/HK1_Nam3_2026/KTHDV/SOA_code/Group8_APITasks/README.md) (Gốc dự án)
  - Phối hợp trong `task-api/paths/auth.yaml` & `task-api/components/`
  - Kiểm thử chất lượng (QA) toàn bộ file `openAI.yaml`
* **Công việc cụ thể cần làm:**
  1. **Phối hợp cùng TV1 hoàn thiện phân hệ Auth & Common Components:**
     - Cùng TV1 rà soát, kiểm thử các endpoints trong `auth.yaml` (`login`, `register`, `me`).
     - Bổ sung, tinh chỉnh các mô tả lỗi trong `responses.yaml` và `schemas.yaml` nếu cần.
  2. **Kiểm thử chất lượng toàn cục (QA & Testing):**
     - Dùng extension **OpenAPI (Swagger) Editor** mở file `openAI.yaml` để kiểm tra preview toàn diện.
     - Đảm bảo tất cả các đường dẫn `$ref` của TV2, TV3, TV4 sau khi viết xong đều hoạt động trơn tru, không báo đỏ hay lỗi cú pháp YAML nào.
  3. **Chịu trách nhiệm viết hoàn chỉnh tài liệu `README.md`:**
     - Cập nhật đầy đủ thông tin nhóm: Tên nhóm, tên môn, danh sách 5 thành viên kèm Mã sinh viên.
     - Giới thiệu tổng quan về hệ thống Book Management API.
     - Viết hướng dẫn chi tiết cách mở/xem tài liệu API (bằng Swagger Editor trong IDE hoặc Online).
     - Chụp ảnh minh họa giao diện Swagger UI đẹp mắt sau khi hoàn thiện và đưa vào file README.

---

## IV. QUY CHUẨN KỸ THUẬT VÀ PHỐI HỢP GIT

### 1. Quy tắc viết YAML chuẩn:
- **Thụt lề:** Bắt buộc thụt lề bằng **2 dấu cách (Space)**, tuyệt đối **không dùng phím TAB**.
- **Tái sử dụng bằng `$ref`:**
  - Gọi Schema: `$ref: "../components/schemas.yaml#/<TênSchema>"`
  - Gọi Response lỗi: `$ref: "../components/responses.yaml#/<TênLỗi>"`
- **Mã HTTP chuẩn RESTful:**
  - `200`: Thành công cho GET, PUT.
  - `201`: Tạo mới thành công cho POST.
  - `204`: Xóa thành công cho DELETE.
  - `400`: Dữ liệu gửi lên sai (Bad Request).
  - `401`: Chưa xác thực / token sai (Unauthorized).
  - `404`: Không tìm thấy bản ghi theo ID (Not Found).
