%not meant to run, didnt create f[]

%optimize for a 4 cycle latency fully pipelined ADD unit. the throughput is
%1 add per cycle
sum=0;
for i=0:N-1
    sum=sum+f[i];
end

%optimized code
sum=0;
i=0;
for i:N-1
    sum=sum+f[i]
end