def get_response():
    call_counter = 1
    while True:
        response = [i for i in range(call_counter, call_counter + 10)]
        call_counter += 10
        yield response


class Pagination:
    def __init__(self, current, step):
        self.current = current
        self.responses = []
        self.step = step
        self.available = 0
        self.response_generator = get_response()
        self.call_count = 0

    def get_n_elements(self, n):
        while self.available < self.current+n:
            self.call_count += 1
            self.responses.extend(next(self.response_generator))
            self.available += self.step

        current_chunk, self.responses = self.responses[:n], self.responses[n:]
        self.current += n
        return current_chunk


if __name__ == "__main__":
    p = Pagination(0, 10)
    print(p.get_n_elements(6))
    print(p.get_n_elements(17))
    print(p.get_n_elements(3))
    print(p.get_n_elements(2))
    print(p.get_n_elements(1))
    print(p.get_n_elements(1))
    print(p.get_n_elements(1))
    print(p.call_count)
