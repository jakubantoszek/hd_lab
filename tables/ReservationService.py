class ReservationService:
    def __init__(self, reservation, worker, text):
        if text is None:
            self.reservation_id = reservation
            self.worker_id = worker
        else:
            values = text.split('|')
            self.reservation_id = values[0]
            self.worker_id = values[1]

    def __str__(self):
        return "%s|%s" % (self.reservation_id, self.worker_id)
