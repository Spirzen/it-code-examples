type server struct {
    pb.UnimplementedPhoneBookServer
    db map[string]string
}

func (s *server) Get(ctx context.Context, req *pb.GetRequest) (*pb.GetResponse, error) {
    phone, ok := s.db[req.GetName()]
    if !ok {
        return nil, status.Errorf(codes.NotFound, "contact %q", req.GetName())
    }
    return &pb.GetResponse{
        Contact: &pb.Contact{Name: req.GetName(), Phone: phone},
    }, nil
}

func main() {
    lis, err := net.Listen("tcp", ":50051")
    if err != nil {
        log.Fatal(err)
    }
    s := grpc.NewServer()
    pb.RegisterPhoneBookServer(s, &server{db: map[string]string{"Ann": "+1-555-0100"}})
    log.Fatal(s.Serve(lis))
}
