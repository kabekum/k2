from apps.clients.models import Client
from apps.matters.models import Matter

class ConflictDetector:
    """
    Detects conflicts based on historical client relationships
    """

    @staticmethod
    def check_conflict(new_client_name: str):
        conflicts = []

        clients = Client.objects.filter(name__icontains=new_client_name)
        for client in clients:
            matters = Matter.objects.filter(client=client)
            conflicts.append({
                "client": client.name,
                "matter_count": matters.count()
            })

        return conflicts
