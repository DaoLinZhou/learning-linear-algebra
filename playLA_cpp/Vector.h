//
// Created by Daolin on 2019/12/3.
//

#ifndef PLAY_WITH_LINEAR_ALGEBRA_VECTOR_H
#define PLAY_WITH_LINEAR_ALGEBRA_VECTOR_H

#include <iostream>
#include <vector>
#include <cassert>


using namespace std;

template <typename T>
class Vector {
private:
    int size;
    T* values;

public:
    Vector(T* lst, int size){
        this->size = size;
        values = new T[size];
        for(int i = 0; i < size; i++)
            values[i] = lst[i];
    }

    Vector(vector<T> vec){
        this->size = vec.size();
        values = new T[size];
        for(int i = 0; i < size; i++)
            values[i] = vec[i];
    }

    ~Vector(){
        delete[] values;
    }

    T operator[](int index) const;
    int getSize() const;
    int getLength() const;

    Vector<T> operator+(const Vector& v) const;
    Vector<T> operator-(const Vector& v) const;

    Vector<T> operator*(double k) const;

    Vector<T> operator+() const;
    Vector<T> operator-() const;

    template <typename Type>
    friend Vector<Type> operator*(double k, const Vector<Type>& v);

    template <typename Type>
    friend ostream& operator<<(ostream& out, const Vector<Type>& v);

};




#endif //PLAY_WITH_LINEAR_ALGEBRA_VECTOR_H
