# 🛍️ Retail POS Software  

## 📌 Overview  
The Retail POS Software is a **point-of-sale system for walk-in retail customers**. It allows shop owners and cashiers to:  
- Manage products and categories.  
- Record sales transactions.  
- Accept **cash or mobile money payments** (MTN MoMo & Telecel Cash).  
- Track inventory automatically when sales are made.  
- View sales history for reporting and auditing.  

This system is ideal for **retail shops, supermarkets, and small businesses** that need a simple but powerful POS solution.  

---

## 🔄 Workflow  

### 1. Products & Inventory  
- Admin or staff adds products to the system (with prices and stock levels).  
- Products are grouped into categories (e.g., Beverages, Snacks, Electronics).  
- Stock updates automatically whenever a sale is made.  

### 2. Walk-in Customers  
- Default sales are made to **“walk-in customers”** (no need for customer registration).  
- Optional customer details can be added if needed (future feature).  

### 3. Sales Process (Checkout Flow)  
1. Cashier searches and selects products.  
2. Products are added to a **cart** with quantities.  
3. The system calculates the total.  
4. Cashier selects **payment method**:  
   - **Cash** → Sale is marked as completed instantly.  
   - **MTN MoMo** → Initiates a mobile money request to the customer’s phone.  
   - **Telecel Cash** → Same flow as MoMo but with Telecel’s API.  
5. If mobile money is used, system verifies transaction before marking the sale as **completed**.  
6. A receipt is generated with details: products, quantities, payment method, and transaction reference (for MoMo/Telecel).  

### 4. Payments  
- **Cash**: Simple, instant, no external API required.  
- **Mobile Money**:  
  - Supports MTN MoMo and Telecel Cash.  
  - Integration is done through their official APIs.  
  - Each transaction gets a reference ID for verification.  

### 5. Reporting & Tracking  
- Sales history can be viewed by date.  
- Each sale stores products, total amount, payment method, and status.  
- Inventory reduces automatically when sales happen.  

---

## 🖥️ How People Can Use It  

- **Cashiers**  
  - Search for products quickly.  
  - Add items to customer’s cart.  
  - Choose payment method (cash, MoMo, Telecel).  
  - Generate and print receipts.  

- **Shop Owners / Managers**  
  - Manage products and stock levels.  
  - Track daily sales.  
  - Check payment records and verify mobile money transactions.  
  - Get insights into best-selling products and revenue trends (future reporting features).  

- **Customers**  
  - Simply pay for their items via cash, MTN MoMo, or Telecel Cash.  
  - Receive a receipt confirming their purchase.  

---

## ⚡ Tech Stack  
- **Backend:** Django + Django REST Framework  
- **Frontend:** React (planned)  
- **Database:** SQLite (development) / PostgreSQL (production)  
- **Payments:** MTN MoMo API & Telecel Cash API  

---

## 📌 Roadmap  
- ✅ Products and Sales workflows built.  
- 🔄 Integrate MTN MoMo API.  
- 🔄 Integrate Telecel Cash API.  
- 🔜 Build POS frontend interface (cart, checkout, payments).  
- 🔜 Add sales reports & analytics.  
