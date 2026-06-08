// contracts/ProfileDataContracts.cs
public record UserProfileMinimal(
    Guid UserId,
    string DisplayName,
    string PhoneNumberMasked
);

public record DeliveryAddress(
    string Street,
    string Building,
    string Apartment,
    string EntranceCode,
    double Latitude,
    double Longitude
);

public interface IProfileDataService
{
    Task<UserProfileMinimal> GetMinimalProfileAsync(Guid userId);
    Task<DeliveryAddress> GetDefaultDeliveryAddressAsync(Guid userId);
    Task<bool> HasPaymentMethodsAsync(Guid userId);
}

// Реализация сервиса в ядре
public class ProfileDataService : IProfileDataService
{
    private readonly IUserDataRepository _userDataRepository;
    
    public ProfileDataService(IUserDataRepository userDataRepository)
    {
        _userDataRepository = userDataRepository;
    }
    
    public async Task<UserProfileMinimal> GetMinimalProfileAsync(Guid userId)
    {
        var userData = await _userDataRepository.GetByIdAsync(userId);
        return new UserProfileMinimal(
            userId,
            userData.FirstName + " " + userData.LastName[0] + ".",
            MaskPhoneNumber(userData.PhoneNumber)
        );
    }
    
    private string MaskPhoneNumber(string phone)
    {
        return phone.Length > 6 
            ? phone.Substring(0, 3) + "****" + phone.Substring(phone.Length - 2)
            : "******";
    }
}
