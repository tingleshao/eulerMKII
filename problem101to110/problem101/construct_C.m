function [ c ] = construct_C( n )
%CONSTRUCT_C Summary of this function goes here
%   Detailed explanation goes here
for i = 1:n-1
    c(i) = n^(i-1);
end

end

