class Job:
    def __init__(self, data: dict):
        self.assigned_tunnel_id: int = data.get('assigned_tunnel_id')
        self.device_type: str = data.get('device_type')
        self.owner_sauce: str = data.get('owner_sauce')
        self.consolidated_status: str = data.get('consolidated_status')
        self.id: str = data.get('id')
        self.name: str = data.get('name')
        self.os: str = data.get('os')
        self.os_version: str = data.get('os_version')
        self.device_name: str = data.get('device_name')
        self.status: str = data.get('status')
        self.automation_backend: str = data.get('automation_backend')
        self.manual: bool = data.get('manual')
        self.creation_time: int = data.get('creation_time')
        self.start_time: int = data.get('start_time')
        self.end_time: int = data.get('end_time')

    def __str__(self):
        return self.name
