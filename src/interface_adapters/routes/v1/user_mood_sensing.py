from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from domain.use_cases.happy_location import HappyLocationUseCase
from domain.use_cases.mood_frequency import MoodFrequencyUseCase
from frameworks.container import FrameworkContainer
from interface_adapters.dtos.happy_location import HappyLocationOutputDTO
from interface_adapters.dtos.mood_frequency import MoodFrequencyOutputDTO

mood_frequency_route = APIRouter()
happy_location_route = APIRouter()


@mood_frequency_route.get("/mood/frequency/{user_name}", response_model=MoodFrequencyOutputDTO)
@inject
async def mood_frequency(
    user_name: str,
    use_case: MoodFrequencyUseCase = Depends(
        Provide[FrameworkContainer.mood_frequency_use_case]
    ),
) -> MoodFrequencyOutputDTO:
    """Route get mood frequency"""
    try:
        output_use_case = await use_case(user_name=user_name)

        return MoodFrequencyOutputDTO(
            result=output_use_case.result
        )
    except Exception as error:
        return {"error": f"{error}"}


@happy_location_route.get("/happy/location/{user_name}", response_model=HappyLocationOutputDTO)
@inject
async def happy_location(
    user_name: str,
    use_case: HappyLocationUseCase = Depends(
        Provide[FrameworkContainer.happy_location_use_case]
    ),
) -> HappyLocationOutputDTO:
    """Route get happy location"""
    try:
        output_use_case = await use_case(user_name=user_name)
        print(output_use_case)
        return HappyLocationOutputDTO(
            user_name=output_use_case.user_name,
            happy_frequency=output_use_case.happy_frequency,
            location=output_use_case.location,
        )
    except Exception as error:
        return {"error": f"{error}"}
