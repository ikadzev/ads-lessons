#include <stdio.h>
#include <stdlib.h>

void nullCheck(void* ptr) {
    if (ptr == NULL) {
        printf("OoM!");
        exit(1);
    }
}

typedef struct {
    int* data;
    size_t length;
    size_t capacity;
} DynArrStr;

void initDynArrStr(DynArrStr* arr) {
    arr->length = 0;
    arr->capacity = 2;
    arr->data = (int*)malloc(arr->capacity * sizeof(int));
    nullCheck(arr->data);
}

void freeDynArrStr(DynArrStr* arr) {
    free(arr->data);
    arr->length = 0;
    arr->capacity = 0;
}

void removeFromArr(DynArrStr* arr) {
    if (arr->length != 0) {
        if (arr->length * 4 < arr->capacity) {
            arr->capacity = arr->length;
            arr->data = (int*)realloc(arr->data, arr->capacity * sizeof(int));
            nullCheck(arr->data);
        }
        arr->length--;
    } else {
        printf("Удаление из пустого списка!\n");
    }

}

void appendDynArrStr(DynArrStr* arr, int num) {
    if (arr->length >= arr->capacity) {
        arr->capacity *= 2;
        arr->data = (int*)realloc(arr->data, arr->capacity * sizeof(int));
        nullCheck(arr->data);
    }
    arr->data[arr->length++] = num;
}

int returnElement(DynArrStr* arr, size_t index) {
    if (index < arr->length) {
        return arr->data[index];
    } else {
        printf("Неправильный индекс!\n");
        return -1;
    }
}

void printDArr(DynArrStr* arr) {
    for (size_t i = 0; i < arr->length; i++) {
        printf("%d ", arr->data[i]);
    }
    printf("\n");
}


int main() {
    DynArrStr darr;
    initDynArrStr(&darr);
    while (1) {
    printf("Введите действие с массивом:\n");
    printf("1. Доступ к элементу\n");
    printf("2. Добавление элемента\n");
    printf("3. Удаление последнего элемента\n");
    printf("0. Exit\n");
    int check;
    scanf("%d", &check);
    switch (check) {
    	case 1:
	    if (darr.length == 0) {
	    	printf("Массив пустой!\n");
	    	continue;
	    }
    	    size_t index;
    	    printf("Индекс? ");
    	    scanf("%lu", &index);
    	    printf("%d\n", returnElement(&darr, index));
    	    continue;
    	case 2:
    	    int number;
    	    printf("Число? ");
    	    scanf("%d", &number);
    	    appendDynArrStr(&darr, number);
    	    continue;
    	case 3:
    	    removeFromArr(&darr);
    	    continue;
    	case 0:
    	    exit(0);
    }
    }
    return 0;
}
