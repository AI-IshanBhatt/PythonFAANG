"""
You have a http_service or a library function that you can not change.
It provides you 10 elements at a time.
Once you have gotten the 10 elements you can not request them again.



You are supposed to build an efficient client/class, such that when you call get_n_elements gives you n elements.
get_n_elements(7)  - 1,7 elements
get_n_elements(10) - 8,17 elements
get_n_elements(1)  - 18th element
get_n_elements(35)  - 19th to 44th element
"""
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
        # self.response_generator = get_response()

    def get_n_elements(self, n):
        while self.available < self.current+n:
            self.responses.extend(next(get_response()))
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
    print(p.get_n_elements(35))


