# 📧 Bulk Email to SMS Tool

## 📖 Introduction
The Bulk Email to SMS Tool is designed to help businesses and individuals send bulk SMS messages through email. This tool leverages email-to-SMS gateways provided by mobile carriers to convert and send emails as SMS messages to recipients' mobile phones.

## 🛠️ How It Works
The tool takes a list of email addresses and messages, converts them into SMS format, and sends them to the recipients using email-to-SMS gateways. It supports various mobile carriers and ensures that messages are delivered efficiently.

## ✨ Features
- **📨 Bulk Sending**: Send SMS messages to multiple recipients at once.
- **📡 Carrier Support**: Supports major mobile carriers with email-to-SMS gateways.
- **📝 Customizable Templates**: Use customizable templates for your messages.
- **📈 Delivery Reports**: Get delivery reports for sent messages.
- **🌐 User Interface**: Web-based interface for managing and sending SMS messages.

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/coderprasnt/bulk-email-to-sms.git
cd bulk-email-to-sms
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure the tool
- Create a configuration file `config.json` in the root directory with your email and SMS gateway settings.
- Example `config.json`:
```json
{
    "email": {
        "smtp_server": "smtp.your-email-provider.com",
        "smtp_port": 587,
        "username": "your-email@example.com",
        "password": "your-email-password"
    },
    "sms_gateways": {
        "verizon": "vtext.com",
        "att": "txt.att.net",
        "tmobile": "tmomail.net"
    }
}
```

### 4. Run the tool
```bash
python send_sms.py --recipients recipients.csv --message "Your message here"
```

## 🚀 Usage

### Sending SMS
To send SMS messages, use the following command:
```bash
python send_sms.py --recipients path/to/recipients.csv --message "Your message here"
```

### Example
1. **📄 Prepare the recipients list**:
    - Create a CSV file `recipients.csv` with the following format:
    ```csv
    phone_number,carrier
    1234567890,verizon
    0987654321,att
    ```

2. **📤 Send the SMS**:
    ```bash
    python send_sms.py --recipients recipients.csv --message "Your message here"
    ```

## 🏁 Conclusion
The Bulk Email to SMS Tool is a powerful solution for sending bulk SMS messages through email. By leveraging email-to-SMS gateways, it provides an efficient way to reach your audience via SMS.

## 📞 Contact
If you have any questions or need further assistance, please contact us through our Telegram channel.

- **Telegram**: [WitchShopHub](https://t.me/witchshophub)
