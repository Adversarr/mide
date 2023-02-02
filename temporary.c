int x[2];


int sum(int x, int y) {
    int a;
    int b;
    a = x - 1;
    b = y + 1;
    return a + b;
}

int sleep(int clock) {
   int i;
   i = 0;
   while (i < clock) { i = i + 1; }
}
int main(void) {
    int z;
    int i;
    z = sum(3, 4);

    while (1) {
        sleep(102400);
        i = $(0xFFFFFC70);
        z = z + 1;
        $(0xFFFFFC60) = i + z;
    }
    return 0;
}