"""Scanner-only leak demo (FAKE / NON-FUNCTIONAL).

This module is intentionally full of hardcoded "sensitive" strings to test secret/PII detection.
It is NOT imported by the FastAPI app.

All values below are fake and intentionally malformed so they do not represent usable credentials.
"""

# --- Generic app secrets (fake) ---
API_KEY = "api_key_FAKE-1234-DO-NOT-USE"
JWT_SECRET = "jwt_secret_NOT-REAL_change-me"
SESSION_SECRET = "session_secret_NOT_REAL_please_rotate"
ENCRYPTION_KEY_LIKE = "enc_key_FAKE_32bytes_xxxxxxxxxxxxxxxxxxxxxxxx"

# --- Database / service config (fake) ---
DB_USER = "db_admin_fake"
DB_PASSWORD = "password_NOT_REAL_1234"
DATABASE_URL_LIKE = "postgresql://db_admin_fake:password_NOT_REAL_1234@127.0.0.1:5432/fake_db"
REDIS_URL_LIKE = "redis://:redis_password_NOT_REAL@127.0.0.1:6379/0"

# --- Token-like strings (intentionally broken so they are non-usable) ---
GITHUB_TOKEN_LIKE = "ghpX_NOTAREAL_TOKEN_XXXXXXXXXXXXXXXXXXXX"  # looks like ghp_ but broken
GITLAB_TOKEN_LIKE = "glpatX_FAKE_TOKEN_XXXXXXXXXXXXXXXXXXXX"  # looks like glpat- but broken
SLACK_BOT_TOKEN_LIKE = "xoxbX-000000000000-0000000000000-FAKE"  # looks like xoxb- but broken
STRIPE_SECRET_LIKE = "sk_l1ve_FAKE_XXXXXXXXXXXXXXXXXXXXXXXX"  # looks like sk_live_ but broken
SENDGRID_API_KEY_LIKE = "SGX.FAKE_PART_1.FAKE_PART_2"  # looks like SG. but broken
GOOGLE_API_KEY_LIKE = "AIzaXFAKE-KEY-WITH-BROKEN-PREFIX"  # looks like AIza but broken

# AWS-like (intentionally breaks real patterns)
AWS_ACCESS_KEY_LIKE = "AKIAX_FAKE_KEY_0000"  # breaks the real AKIA pattern
AWS_SECRET_KEY_LIKE = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYFAKE"  # fake

# --- Private key-ish blocks (broken headers on purpose) ---
SSH_PRIVATE_KEY_LIKE = (
    "-----BEGIN 0PENSSH PR1VATE KEY-----\n"
    "b3BlbnNzaC1rZXktdjEAAAAABGZha2UAAAAB\n"
    "-----END 0PENSSH PR1VATE KEY-----\n"
)

# --- PII-like data (fake) ---
ADMIN_EMAIL = "admin@example.invalid"
SUPPORT_EMAIL = "support@example.invalid"
SUPPORT_PHONE = "+82-10-0000-0000"

# IDs / numbers that resemble real formats but are explicitly fake
KOREAN_RRN_LIKE = "900101-0000000"  # fake
PASSPORT_LIKE = "M00000000"  # fake
DRIVER_LICENSE_LIKE = "11-00-000000-00"  # fake

# Payment-like (test-only / non-usable)
CREDIT_CARD_TEST_LIKE = "4242 4242 4242 4242"  # common test number (not a real card)
CVC_LIKE = "000"

# Addresses (fake)
HOME_ADDRESS = "123 Fake St, Test City, ZZ 00000"
