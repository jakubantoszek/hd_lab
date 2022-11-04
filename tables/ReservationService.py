class ReservationService:
    def __init__(self, reservation, worker):
        self.reservation_id = reservation
        self.worker_id = worker

    def __str__(self):
        return "%s|%s" % (self.reservation_id, self.worker_id)
