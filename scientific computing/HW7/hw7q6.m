%Write your own matrix multiplication code and recreate the graph from
%the "Core i7 Matrix Multiply Performance" slide


%essentially run a matrix multiplication for each style
%(ijk,ikj,jki,kji,jik,kij) 
%record the cycles per inner loop iteration for each 
%array size N 50:50:700
%graph the result

%NOTE- I can't seem to figure out how to get the cycles per inner loop
%count so I'll be excluding this from my program

%ijk
clear; clc;
for N=50:50:700
    c=zeros(N);
    a=ones(N);
    b=ones(N);
    %this is where I would insert the cycles per inner loop variable
    %and begin recording the cycles elapsed
    for i=1:N
        for j=1:N
            sum=0;
            for k=1:N
                sum = sum + (a(i,k) * b(k,j));
                c(i,j) = sum;
            end
        end
    end
    %this is where I would end the cycles per inner loop value
    %the counter would be recorded in an additive vector
end

%jik
clear; clc;
for N=50:50:700
    c=zeros(N);
    a=ones(N);
    b=ones(N);
    %this is where I would insert the cycles per inner loop variable
    %and begin recording the cycles elapsed
    for j=1:N
        for i=1:N
            sum=0;
            for k=1:N
                sum = sum + (a(i,k) * b(k,j));
                c(i,j) = sum;
            end
        end
    end
    %this is where I would end the cycles per inner loop value
    %the counter would be recorded in an additive vector
end

%repeat this for the other 4 styles and assemble a
%graph of cycles per inner loop vs. array size (N)