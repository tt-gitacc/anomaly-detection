This script can detect anomalies within the following dataset: http://lib.stat.cmu.edu/datasets/sleep<br>
Every time it runs, it will..<br>
  1. store each attribute into an array<br>
  2. calculate the mean of each attribute in the array<br>
  3. calculate the standard deviation of each attribute in the array<br>
  4. loop through each value in the array to determine whether or not it is anomalous. If the iterator is greater than "the mean plus (or minus) two, multiplied by its standard deviation," the following statement will be returned: "[iterator] is an anomalous value"<br>
