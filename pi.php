<?php

$diameter = 10000;

echo "Calculate PI by precision of " . ($diameter*$diameter).  " tries" . PHP_EOL;

$dots_in_circle = 0;
$dots_total = 0;
$center = $diameter/2;
$radius = $diameter/2;

for ($i=0; $i< $diameter; $i++) {
    for ($j=0; $j< $diameter; $j++) {
        $dots_total++;
        $x_distance_from_center = $center-$i;
        if ($x_distance_from_center< 0) {
            $x_distance_from_center *= -1;
        }
        $y_distance_from_center = $center-$j;
        if ($y_distance_from_center< 0) {
            $y_distance_from_center *= -1;
        }

        $distance_from_center = sqrt($x_distance_from_center*$x_distance_from_center+ $y_distance_from_center*$y_distance_from_center);
        if ($distance_from_center <= $radius) {
            $dots_in_circle++;
        }
    }
}

echo $dots_in_circle . ", " . $dots_total . PHP_EOL;
echo (4*($dots_in_circle/$dots_total));
