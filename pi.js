const diameter = 10000

console.log("Calculate PI by precision of " + diameter*diameter+  " tries")

let dots_in_circle = 0
let dots_total = 0
let center = diameter/2
let radius = diameter/2

for (let i=0; i<diameter; i++) {
    for (let j=0; j< diameter; j++) {
        dots_total++

        let x_distance_from_center = center-i
        if (x_distance_from_center < 0) {
            x_distance_from_center *= -1
        }
        let y_distance_from_center = center-j
        if (y_distance_from_center < 0) {
            y_distance_from_center *= -1
        }

        let distance_from_center = Math.sqrt(x_distance_from_center*x_distance_from_center+y_distance_from_center*y_distance_from_center)
        if (distance_from_center <= radius) {
            dots_in_circle++
        }
    }
}

console.log(dots_in_circle+", "+dots_total)
console.log(4*(dots_in_circle/dots_total))