clear; clc;
%optimize the following matlab matrix multiplication code

for i=1:N
    for j=1:N
        for k=1:N
            c(i,j) = a(i,k) * b(k,j);
        end
    end
end

%optimized code to follow

%the amount of times you run matrix multiplication must be minimized

for i=1:N
    for k=1:N
        r = a(i,k);
        for j=1:N
            c(i,j)= r*b(k,j);
        end
    end
end