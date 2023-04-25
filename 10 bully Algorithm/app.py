import time

class BullyAlgorithm:
    def __init__(self, process_id, processes):
        self.process_id = process_id
        self.processes = processes
        self.coordinator = None

    def start_election(self):
        print(f"Process {self.process_id} starts an election")
        max_id = max(self.processes)
        if self.process_id == max_id:
            self.coordinator = self.process_id
            print(f"Process {self.process_id} is elected as the coordinator")
        else:
            higher_processes = [p for p in self.processes if p > self.process_id]
            for p in higher_processes:
                try:
                    print(f"Process {self.process_id} sends an election message to process {p}")
                    time.sleep(1)
                    response = self.send_message(p, "election")
                    if response == "ok":
                        print(f"Process {p} responded with ok")
                        continue
                    else:
                        print(f"Process {p} did not respond, so Process {self.process_id} starts another election")
                        self.start_election()
                        return
                except:
                    print(f"Process {p} did not respond, so Process {self.process_id} starts another election")
                    self.start_election()
                    return
            self.coordinator = max(higher_processes)
            print(f"Process {self.process_id} recognizes Process {self.coordinator} as the coordinator")

    def send_message(self, process_id, message):
        if process_id not in self.processes:
            return "error"
        if message == "election":
            return "ok"
        elif message == "ok":
            return "ok"
        elif message == "coordinator":
            self.coordinator = process_id
            return "ok"
        else:
            return "error"

if __name__ == '__main__':
    processes = [1, 2, 3, 4, 5]
    process_id = int(input(f"Enter process ID (from {processes}): "))
    bully = BullyAlgorithm(process_id, processes)
    bully.start_election()
