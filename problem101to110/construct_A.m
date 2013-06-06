function [ A ] = construct_A( n )
%CONSTRUCT_A Summary of this function goes here
%   Detailed explanation goes here
for i = 1 : n
    for j = 1 : n
        A(i,j) = i^(j-1);
    end
end


end

