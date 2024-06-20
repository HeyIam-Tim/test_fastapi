from fastapi import APIRouter

from .tasks import send_email_report_dashboard

router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report():
    send_email_report_dashboard.delay('user')

    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
