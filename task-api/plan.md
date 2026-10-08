# HƯỚNG DẪN THỰC HIỆN DỰ ÁN: OPENAPI YAML QUẢN LÝ SÁCH (TASK-API)

---

## I. PHÂN TÍCH YÊU CẦU DỰ ÁN

### 1. Mục tiêu cốt lõi
* **Tên Repository (GitHub):** `task-api` (nằm trong GitHub Organization hoặc tài khoản nhóm).
* **Nhiệm vụ chính:** Tải/Tạo và hoàn thiện file cấu hình **OpenAPI (YAML)** dùng để thiết kế tài liệu API cho một hệ thống **Quản lý sách** (Book Management System).
* **Hình thức làm việc:** Làm theo nhóm (5 thành viên).

### 2. Đầu ra dự kiến (Deliverables)
* File `openapi.yaml` (hoặc `swagger.yaml`) hoàn chỉnh, chuẩn hóa theo specification OpenAPI 3.0.x (hoặc 3.1.0).
* Thư mục dự án trên GitHub với quy trình Git flow rõ ràng (Branching, Pull Request, Code Review).
* Tài liệu README.md hướng dẫn xem/chạy API Spec (sử dụng Swagger UI / Redoc / Stoplight Studio).

---

## II. QUY TRÌNH HƯỚNG DẪN THỰC HIỆN TỪNG BƯỚC

### **Bước 1: Khởi tạo Repository và Quy chuẩn nhóm**
1. Tạo repo `task-api` trên GitHub.
2. Thiết lập branch protection rule cho nhánh `main` / `master` (bắt buộc phải có PR & review trước khi merge).
3. Thống nhất quy chuẩn thiết kế RESTful API (naming convention, HTTP status code, kiểu dữ liệu chung).

### **Bước 2: Phân tích Thực thể (Entities) & Chức năng (Endpoints)**
Hệ thống Quản lý sách về cơ bản gồm các thực thể chính:
* **Books (Sách):** ID, tiêu đề, tác giả, danh mục, giá, số lượng, năm xuất bản...
* **Authors (Tác giả):** ID, tên, tiểu sử, ngày sinh...
* **Categories (Danh mục/Thể loại):** ID, tên danh mục, mô tả...
* **Users / Authentication (Người dùng & Xác thực):** Đăng nhập, đăng ký, cấp Token (Bearer Auth)...

### **Bước 3: Xây dựng File OpenAPI YAML**
Mỗi thành viên làm việc trên branch cá nhân (`feature/name-task`) và viết phần YAML được giao:
* Định nghĩa **Paths** (URL, Method: GET, POST, PUT, DELETE, các tham số request/response).
* Định nghĩa **Components/Schemas** (Cấu trúc dữ liệu tái sử dụng).
* Định nghĩa **SecuritySchemes** (Cấu hình JWT / API Key).

### **Bước 4: Kiểm thử, Review và Merge**
1. Sử dụng công cụ validate YAML/OpenAPI (như Swagger Editor, Redocly CLI, hoặc VS Code Extension *OpenAPI (Swagger) Editor*).
2. Tạo Pull Request (PR) về `main`. Các thành viên khác tiến hành review và phê duyệt.
3. Merge code và kiểm tra tính hoàn chỉnh trên nhánh `main`.

---

## III. PHÂN CHIA NHIỆM VỤ CHO NHÓM 5 NGƯỜI

Để đảm bảo khối lượng công việc cân bằng và đúng quy trình làm việc nhóm, công việc được chia cụ thể như sau:

---

### **Thành viên 1: Team Leader / DevOps & Authentication API**
* **Trách nhiệm chính:**
  * Tạo Repository `task-api`, thiết lập cấu trúc file ban đầu (`openapi.yaml`, `.gitignore`, `README.md`).
  * Định nghĩa thông tin chung trong `openapi.yaml`: `openapi`, `info`, `servers`, `tags`, `securitySchemes` (JWT Bearer Auth).
  * Viết API phần Authentication/User:
    * `POST /auth/login`
    * `POST /auth/register`
    * `GET /auth/me`
* **Đầu ra:** Khung chuẩn dự án + Phân hệ Auth/User + File README hướng dẫn.

---

### **Thành viên 2: API Quản lý Sách (Core - Part 1: Query & Detail)**
* **Trách nhiệm chính:**
  * Thiết kế Schema `Book` trong phần `components/schemas`.
  * Viết các API truy vấn sách:
    * `GET /books` (Lấy danh sách sách, hỗ trợ phân trang `page`, `limit`, tìm kiếm theo `title`, lọc theo `category_id`).
    * `GET /books/{id}` (Xem chi tiết 1 cuốn sách).
* **Đầu ra:** Các endpoint lấy dữ liệu sách + Schema chi tiết của Book.

---

### **Thành viên 3: API Quản lý Sách (Core - Part 2: CRUD Mutate)**
* **Trách nhiệm chính:**
  * Tái sử dụng Schema `Book` để xây dựng các API thao tác dữ liệu:
    * `POST /books` (Thêm sách mới - yêu cầu Authentication).
    * `PUT /books/{id}` (Cập nhật thông tin sách).
    * `DELETE /books/{id}` (Xóa sách).
  * Định nghĩa các Schema Request Body cho Create/Update Book (`BookCreateInput`, `BookUpdateInput`).
* **Đầu ra:** Các endpoint cập nhật/xóa/thêm sách + Validation Request Schemas.

---

### **Thành viên 4: API Quản lý Tác giả & Danh mục (Authors & Categories)**
* **Trách nhiệm chính:**
  * Thiết kế Schemas `Author` và `Category`.
  * Viết các API Quản lý Tác giả và Danh mục:
    * `GET /categories`, `POST /categories`
    * `GET /authors`, `POST /authors`, `GET /authors/{id}`
  * Liên kết mối quan hệ giữa Book và Author/Category trong Schema.
* **Đầu ra:** Phân hệ Tác giả và Danh mục đầy đủ CRUD cơ bản.

---

### **Thành viên 5: QA / Common Components & Error Handling**
* **Trách nhiệm chính:**
  * Định nghĩa các Schemas dùng chung (Common Schemas):
    * `ErrorResponse` (Cấu trúc báo lỗi chuẩn: status code, message, details).
    * `PaginationMeta` (Thông tin phân trang).
  * Viết các Responses mẫu cho status codes: `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `500 Internal Server Error`.
  * Kiểm thử file `openapi.yaml` toàn cục (linting, syntax check), đảm bảo không bị trùng lặp hoặc lỗi cú pháp YAML.
* **Đầu ra:** Hệ thống báo lỗi chuẩn hóa + | Bước | Người thực hiện | Công việc chính |
| :--- | :--- | :--- |
| 1 | Thành viên 1 | Init Repo + Cấu trúc chung OpenAPI + Auth APIs |
| 2 | Thành viên 5 | Tạo Common Schemas (Error, Pagination) |
| 3 | Thành viên 2, 3, 4 | Viết các Endpoints & Schemas được phân công |
| 4 | Cả 5 người | Tạo PR, Review chéo code của nhau |
| 5 | Thành viên 5 & 1 | Validate file tổng, Merge vào `main`, hoàn thiện README |e của nhau | Ngày 5 |
| 5 | Thành viên 5 & 1 | Validate file tổng, Merge vào `main`, hoàn thiện README | Ngày 6 |

---

## V. CÔNG CỤ KHUYÊN DÙNG
1. **Editor:** Visual Studio Code (Cài extension *OpenAPI (Swagger) Editor* hoặc *Swagger Viewer*).
2. **Online Editor:** [Swagger Editor](https://editor.swagger.io/) (Dùng để dán code YAML kiểm tra giao diện & lỗi hiển thị tức thì).
3. **Linter:** Redocly CLI (`npx @redocly/cli lint openapi.yaml`) để phát hiện lỗi chuẩn hóa.               # Tài liệu bổ trợ / Ảnh chụp Swagger UIc khi merge