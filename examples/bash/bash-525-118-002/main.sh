factorial() {
    local n=$1
    
    if [ "$n" -le 1 ]; then
        echo 1
        return 0
    fi
    
    local prev_result
    prev_result=$(factorial $((n - 1)))
    echo $((n * prev_result))
}

result=$(factorial 5)
echo "Факториал 5 равен: $result"
