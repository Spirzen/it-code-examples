package consistenthash

import (

    "hash/crc32"
    "sort"
    "strconv"
)

type ConsistentHash struct {
    replicas int
    ring     []uint32
    nodeMap  map[uint32]string
}

func NewConsistentHash(replicas int) *ConsistentHash {
    return &ConsistentHash{
        replicas: replicas,
        ring:     make([]uint32, 0),
        nodeMap:  make(map[uint32]string),
    }
}

func (c *ConsistentHash) AddNode(node string) {
    for i := 0; i < c.replicas; i++ {
        hash := crc32.ChecksumIEEE([]byte(strconv.Itoa(i) + node))
        c.ring = append(c.ring, hash)
        c.nodeMap[hash] = node
    }
    sort.Slice(c.ring, func(i, j int) bool {
        return c.ring[i] < c.ring[j]
    })
}

func (c *ConsistentHash) GetNode(key string) string {
    if len(c.ring) == 0 {
        return ""
    }
    
    hash := crc32.ChecksumIEEE([]byte(key))
    idx := sort.Search(len(c.ring), func(i int) bool {
        return c.ring[i] >= hash
    })
    
    if idx == len(c.ring) {
        idx = 0
    }
    
    return c.nodeMap[c.ring[idx]]
}
