FC = gfortran
FFLAGS = -O2 -Wall -std=f2018 -Jmod -Iinclude
OBJDIR = obj
MODDIR = mod

SRCS = main.f90 math.f90 io.f90
OBJS = $(SRCS:.f90=.o)
OBJS := $(OBJS:%=$(OBJDIR)/%)

$(OBJDIR)/%.o: src/%.f90 | $(MODDIR)
	$(FC) $(FFLAGS) -c $< -o $@

$(MODDIR):
	mkdir -p $(MODDIR)

program: $(OBJS)
	$(FC) $(FFLAGS) $^ -o $@

clean:
	rm -rf $(OBJDIR) $(MODDIR) program
