calculate_area() {
    local width=$1
    local height=$2
    echo $((width * height))
}

calculate_perimeter() {
    local width=$1
    local height=$2
    echo $((2 * (width + height)))
}

analyze_shape() {
    local w=$1
    local h=$2
    local area
    local perimeter
    
    area=$(calculate_area "$w" "$h")
    perimeter=$(calculate_perimeter "$w" "$h")
    
    echo "Площадь: $area"
    echo "Периметр: $perimeter"
}

analyze_shape 10 5
