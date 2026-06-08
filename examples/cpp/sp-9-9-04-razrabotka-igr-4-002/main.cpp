// MyActor.cpp
#include "MyActor.h"

AMyActor::AMyActor()
{
    PrimaryActorTick.bCanEverTick = true; // false — если Tick не нужен
}

void AMyActor::BeginPlay()
{
    Super::BeginPlay();
    UE_LOG(LogTemp, Log, TEXT("Actor started"));
}

void AMyActor::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
}
