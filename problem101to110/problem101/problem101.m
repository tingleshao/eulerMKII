clear
for i = 1:10
   a(i) = u_n(i)
end

a
% construct A matrix
sum_fit = 0;
for i = 1:10,
    A = construct_A(i);
    y = a(1:i)';
    b = A\y;
    c = construct_C(i+1);
    fit = (c * b);
    sum_fit = sum_fit + fit;
end
sum_fit

