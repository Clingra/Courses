%calculate monte carlo method by estimating # of points
%needed to get 2,4,8,16 decimal places of accuracy
%effect of single vs double precision?
%run time for 14  decimal places vs ramanuyan's method?

clear; clc; close;

piTo2=3.14; piTo4=3.1416;
piTo8=3.14159265; 
piTo16=3.1415926535897932;

%pi to 2 decimal places
 
piEstimate1=zeros();
circStdDev1=zeros();
i=1;

while round(mean(piEstimate1()),2)~=round(piTo2,2)
    x1=rand();
    y1=rand();
    %^ randomly generating points for amount in numPoints vector
    checkInside=(x1-0.5).^2 + (y1-0.5).^2 < 0.5^2; 
    %^ boolean for inside or outside of circle
    piEstimate1(i)=sum(checkInside)*4/i;
    mean(piEstimate1)
    i=i+1;
end

%ran out of time to submit this
%my pi estimate is where the issue lies

circAvg=mean(piEstimate1); 

fprintf('Monte Carlo to two digit precision: \n');
fprintf('Using %d points: %f \n',numPoints1,circAvg);