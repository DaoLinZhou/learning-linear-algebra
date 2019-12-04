//
// Created by Daolin on 2019/12/3.
//

#include "Vector.h"

template <typename T>
int Vector<T>::getSize() const{
    return size;
}

template <typename T>
int Vector<T>::getLength() const {
    return size;
}

template <typename T>
Vector<T> Vector<T>::operator+(const Vector<T>& v) const{
    assert(v.size == size);
    T temp[size];
    for(int i = 0; i < size; i++)
        temp[i] = values[i] + v[i];
    return Vector<T>(temp, size);
}

template <typename T>
Vector<T> Vector<T>::operator-(const Vector& v) const{
    assert(v.size == size);
    T temp[size];
    for(int i = 0; i < size; i++)
        temp[i] = values[i] - v[i];
    return Vector<T>(temp, size);
}

template <typename T>
Vector<T> Vector<T>::operator*(double k) const{
    T temp[size];
    for(int i = 0; i < size; i++)
        temp[i] = k * values[i];
    return Vector<T>(temp, size);
}

template <typename T>
Vector<T> Vector<T>::operator+() const{
    return *this;
}

template <typename T>
Vector<T> Vector<T>::operator-() const {
    return -1 * (*this);
}

template <typename Type>
Vector<Type> operator*(double k, const Vector<Type>& v){
    return v * k;
}

template <typename Type>
std::ostream& operator<<(ostream& out, const Vector<Type>& v){
    out << "( ";
    for(int i = 0; i < v.size-1; i++)
        out << v[i] << ", ";
    out << v[v.size-1] << " )";
    return out;
}

template <typename T>
T Vector<T>::operator[](int index) const {
    assert(index >= 0 && index < size);
    return values[index];
}

